
class Heap {
    constructor(initialArray=[]){
        // let height = Math.ceil( Math.log(n+1) / Math.log(2) ) // binary tree's height
        this.Heapify(initialArray)
    }

    // Given array, return Heap structure
    Heapify(array){
        this.heapArray = [] // clear up array
        array.forEach( (elm) => this.Insert(elm) )
        return this.heapArray
    }

    // Insert an element at the back and re-sort the tree
    Insert(elm){
        let pos = this.heapArray.push(elm) - 1
        this.BubbleUp(pos)
    }

    FindMin(){
        return this.heapArray[0]
    }

    // 1) Extract the first element
    // 2) fill the first position with the last element
    // 3) re-sort the tree 
    ExtractMin(){
        let min = this.heapArray[0]
        if(this.heapArray.length > 1){
            this.heapArray[0] = this.heapArray.pop()
            this.BubbleDown(0)
        } else {
            this.heapArray = []
        }
        return min

    }

    // 1) delete an element in given position
    // 2) fill the position with the last element
    // 3) re-sort the tree
    Delete(pos){
		if(pos == this.heapArray.length-1)
			this.heapArray.pop()
		else {
			this.swap(pos, this.heapArray.length-1) // swap the element to be deleted with the last item
			let deleted = this.heapArray.pop() // delete the last one
			if(this.heapArray[pos].key > deleted.key)
				this.BubbleUp(pos)
			else if (this.heapArray[pos].key < deleted.key)
				this.BubbleDown(pos)	
		}

    }

    // sort the tree upwards
    BubbleUp(pos){
        if(pos > 0){
            let pos_parent = Math.floor((pos-1)/2) // position of parent = [(i-1)/2]
            if(this.heapArray[pos].score < this.heapArray[pos_parent].score){
                this.swap(pos, pos_parent)
                this.BubbleUp(pos_parent)
            }
        }
        
    }

    // sort the tree downwards
    BubbleDown(pos){
        // position of left-most child = 2i+1
        // position of right-most child = 2i+2
        let pos_left_child = pos * 2 + 1
        let pos_right_child = pos * 2 + 2 
        let pos_smaller_child = 0

        if (pos_right_child <= this.heapArray.length-1){
            if(this.heapArray[pos_left_child].score <= this.heapArray[pos_right_child].score){
                pos_smaller_child = pos_left_child
            } else {
                pos_smaller_child = pos_right_child
            }
        } else if (pos_left_child === this.heapArray.length-1) {
            pos_smaller_child = pos_left_child
        }
        
        if(pos_smaller_child !== 0){
            if(this.heapArray[pos].score > this.heapArray[pos_smaller_child].score){
                this.swap(pos, pos_smaller_child)
                this.BubbleDown(pos_smaller_child)
            }
        }
    }
    
    swap(i, j){
        [this.heapArray[i], this.heapArray[j]] = [this.heapArray[j], this.heapArray[i]]
    }

    print(){
        console.log(this.heapArray)
    }

}


class Vertex {
    constructor(id=0, x=0, y=0, score= Infinity){
        this.id = id
        this.x = x
        this.y = y
        this.score = score
    }
}

class Edge {
    constructor(id, head, tail, length){
        this.id = id
        this.head = head // vertex.id
        this.tail = tail // vertex.id
        this.length = length
    }
}

class Dijkstra {
    constructor(vertices, startingVertexId){
        this.unexplored = new Heap(vertices)
        this.unexplored.heapArray.find(vertex => vertex.id===startingVertexId).score = 0
        this.explored = []
        this.distance = 0
    }
    
    Explore(){
        while(this.unexplored.heapArray.length > 0 ){
            
            let min = this.unexplored.ExtractMin()

            this.explored.push(min)
            this.distance = min.score
            console.log(this.distance)
            edges.forEach((elm)=>{
                if (elm.head === min.id){
                    let idx_elmToUpdate = this.unexplored.heapArray.findIndex(vertex => vertex.id === elm.tail)
                    if(idx_elmToUpdate >= 0 ){
                        let elmToUpdate = this.unexplored.heapArray[idx_elmToUpdate]
                        let oldScore = elmToUpdate.score

                        let newScore = Math.min(oldScore, this.distance + elm.length)
                        // console.log(oldScore, newScore) 
                        let updated = new Vertex(elmToUpdate.id, elmToUpdate.x, elmToUpdate.y, newScore)
                        this.unexplored.Delete(idx_elmToUpdate)
                        this.unexplored.Insert(updated)    
                    }                    
                }
            })

            
        }
    } 

}

// Test Code

var vertices = [new Vertex(0, 0, 0), new Vertex(1, 0, 2), new Vertex(2, 2, 0), new Vertex(3, 2, 2)]
var edges = [new Edge(0, 0, 1, 1), new Edge(1, 0, 2, 3), new Edge(2, 1, 2, 1), new Edge(3, 1, 3, 7), new Edge(4, 2, 3, 4)]

// directed graph
// Vertex(0, 0, 0) means id = 0, 
// Edge(0, 0, 1, 1) means id = 0, head = 0(vertex's id), tail = 1(vertex's id), the edge's length = 1

var my = new Dijkstra(vertices, 0)
my.Explore()
console.log(my.explored)

// Result
// 0: Vertex {id: 0, x: 0, y: 0, score: 0}
// 1: Vertex {id: 1, x: 0, y: 2, score: 1}
// 2: Vertex {id: 2, x: 2, y: 0, score: 2}
// 3: Vertex {id: 3, x: 2, y: 2, score: 6}
