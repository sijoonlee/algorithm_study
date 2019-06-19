class MaxHeap {
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

    FindMax(){
        return this.heapArray[0]
    }

    // 1) Extract the first element
    // 2) fill the first position with the last element
    // 3) re-sort the tree 
    ExtractMax(){
        let max = this.heapArray[0]
        if(this.heapArray.length > 1){
            this.heapArray[0] = this.heapArray.pop()
            this.BubbleDown(0)
        } else {
            this.heapArray = []
        }
        return max

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
            if(this.heapArray[pos].key > this.heapArray[pos_parent].key){
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
        let pos_larger_child = 0

        if (pos_right_child <= this.heapArray.length-1){
            if(this.heapArray[pos_left_child].key >= this.heapArray[pos_right_child].key){
                pos_larger_child = pos_left_child
            } else {
                pos_larger_child = pos_right_child
            }
        } else if (pos_left_child === this.heapArray.length-1) {
            pos_larger_child = pos_left_child
        }
        
        if(pos_larger_child !== 0){
            if(this.heapArray[pos].key < this.heapArray[pos_larger_child].key){
                this.swap(pos, pos_larger_child)
                this.BubbleDown(pos_larger_child)
            }
        }
    }
    
    swap(i, j){
        [this.heapArray[i], this.heapArray[j]] = [this.heapArray[j], this.heapArray[i]]
    }
	
	check(){
		if(this.heapArray.length > 0){
			console.log("1st key", this.heapArray[0].key)
			this.heapArray.forEach( (elm) => {
				if( this.heapArray[0].key <= elm.key )
					console.log("Possible bug: ", elm.key)
			})	
		}
		
	}
			

    print(){
        console.log(this.heapArray)
    }

}


class Vertex{
    constructor(x, y){
        this.x = x
        this.y = y
        this.key = 0
        this.found = false
        this.visited = false
        this.children = []
    }

    setKey = (key) => {
        this.key = key
    }

    setVisited = () => {
        this.visited = true
    }

    getVisited = () => {
        return this.visited
    }

    setFound = () => {
        this.found = true
    }

    getFound = () => {
        return this.found
    }

    getCoordinate = () => {
        return [this.x, this.y]
    }

    addChild = (child) => {
        this.children.push(child)
    }

}

class Grid{
    constructor(column=3, row=3){
        
        this.vertices = []
        this.edges = []
        for(let i = 0; i < row ; i++)
            for(let j = 0; j < column; j++)
                this.vertices.push(new Vertex(j, i))
         
    }

    findVertexByXY = (x,y) => {
        let index = this.vertices.findIndex( (vertex) => {
            let posX = vertex.getCoordinate()[0]
            let posY = vertex.getCoordinate()[1]
            return (posX == x && posY == y)
        } )
        return (index!=-1 ? this.vertices[index] : -1)
       
    }

    findNeighbors = (vertex) => {
        let posX = vertex.getCoordinate()[0]
        let posY = vertex.getCoordinate()[1]
        let neighbors = []
        let possibleWays = [[1,0],[-1,0],[0,1],[0,-1]]
        
        //shuffle array to make more unorganized maze
        //https://stackoverflow.com/questions/6274339/how-can-i-shuffle-an-array
        for (let i = possibleWays.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [possibleWays[i], possibleWays[j]] = [possibleWays[j], possibleWays[i]];
        }
        
        possibleWays.forEach( (way) => {
            let neighbor = this.findVertexByXY(posX + way[0], posY + way[1])
            if (neighbor != -1){
                neighbors.push(neighbor)
            }
        })
        return neighbors
    }
        
}

class Maze{
    constructor(size_x, size_y, starting_x, starting_y){
        this.grid = new Grid(size_y,size_x)
        let start_x = (starting_x == null ? this.getRandomInt(size_x) : starting_x)
        let start_y = (starting_y == null ? this.getRandomInt(size_y) : starting_y)
        
        this.startingVertex = this.grid.findVertexByXY(start_x, start_y)
        this.startingVertex.setFound()
        this.discovered = new MaxHeap()
        this.visitedVertices = []
        this.explore(this.startingVertex)                      
    }

    explore = (vertex) => {

        let key = vertex.key
        vertex.setVisited()
        this.visitedVertices.unshift(vertex) 
            // add element to the front
            // to make array.find() method the lastest item

        let neighbors = this.grid.findNeighbors(vertex)
        neighbors.forEach( (neighbor) => {
            if(neighbor.getFound() == false){
                neighbor.setFound()
                neighbor.setKey(key+1)
                this.discovered.Insert(neighbor)
            } else if(neighbor.getVisited() == false){
                let updateIndex = this.discovered.heapArray.findIndex( (elm) => {
                    let posX = elm.getCoordinate()[0]
                    let posY = elm.getCoordinate()[1]
                    return (posX == neighbor.x && posY == neighbor.y)
                })
                this.discovered.Delete(updateIndex)
                neighbor.setKey(key+1)
                this.discovered.Insert(neighbor)
                
            }
        })

        let next = this.discovered.ExtractMax()
                   
        if(next != null){
            if( next.key == vertex.key+1 ){
                vertex.addChild(next)
             } else if (next.key < vertex.key+1){
				this.visitedVertices.find( (elm) => {
                    return (elm.key == next.key-1)
                }).addChild(next)
				
            } else {
				console.log("Bug Occured!")
			}
            this.explore(next)
        } 
    }
    getRandomInt = (max) => {
        return Math.floor(Math.random() * max);
    }

    getReport = () => {
        return this.visitedVertices
    }
}

class DrawMaze{
    constructor(reportedVertices, canvasID="myCanvas", scale=50){
        this.vertices = reportedVertices
        this.startingVertex = reportedVertices.find( (elm) => {
            return elm.key == 0
        })
        this.scale = scale
        this.canvas = document.getElementById(canvasID)
        this.ctx = this.canvas.getContext("2d")
    }
    clear = () => {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)

    }
    draw = (vertex = this.startingVertex) => {

        if(vertex.key == 0){
            this.ctx.fillSytle = "#FF0000"
        }
        this.ctx.beginPath()
        this.ctx.arc(vertex.x * this.scale + this.scale, vertex.y * this.scale + this.scale, 5, 0, 2*Math.PI);
        this.ctx.closePath()
        this.ctx.fill()
        
        vertex.children.forEach( async (other) => {
            let head_x = vertex.x * this.scale + this.scale
            let head_y = vertex.y * this.scale + this.scale
            let tail_x = other.x * this.scale + this.scale
            let tail_y = other.y * this.scale + this.scale
            this.ctx.moveTo(head_x, head_y)
            this.ctx.lineTo(tail_x, tail_y)
            this.ctx.stroke()
            this.draw(other)
        })
    }
}
    



// const myDrawingBoard = new DrawingBoard(myGrid)
// myDrawingBoard.draw()


document.getElementById("drawMaze").addEventListener("click", () => {
    const myMaze = new Maze(10,10)
    const myDraw = new DrawMaze(myMaze.getReport())
    myDraw.clear()
    myDraw.draw()
}); 


