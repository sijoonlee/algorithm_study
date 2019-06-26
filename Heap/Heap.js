// The Class mimicking the behaviour of Heap data structure
// Written By Sijoon Lee, 2019-6-10

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
        this.heapArray[0] = this.heapArray.pop()
        this.BubbleDown(0)
        return min
    }

    // 1) delete an element in given position
    // 2) fill the position with the last element
    // 3) re-sort the tree
    // 1) delete an element in given position
    // 2) fill the position with the last element
    // 3) re-sort the tree
    Delete(pos){
		if(pos == this.heapArray.length-1)
			this.heapArray.pop()
		else {
			this.swap(pos, this.heapArray.length-1) // swap the element to be deleted with the last item
			let deleted = this.heapArray.pop() // delete the last one
			if(this.heapArray[pos] > deleted)
				this.BubbleUp(pos)
			else if (this.heapArray[pos] < deleted)
				this.BubbleDown(pos)	
		}

    }
    // sort the tree upwards
    BubbleUp(pos){
        if(pos > 0){
            let pos_parent = Math.floor((pos-1)/2) // position of parent = [(i-1)/2]
            if(this.heapArray[pos] < this.heapArray[pos_parent]){
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
            if(this.heapArray[pos_left_child] <= this.heapArray[pos_right_child]){
                pos_smaller_child = pos_left_child
            } else {
                pos_smaller_child = pos_right_child
            }
        } else if (pos_left_child === this.heapArray.length-1) {
            pos_smaller_child = pos_left_child
        }
        
        if(pos_smaller_child !== 0){
            if(this.heapArray[pos] > this.heapArray[pos_smaller_child]){
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


// Test Code
const my = new Heap([6,7,5,10,8,7,9])

my.print()
console.log(my.ExtractMin())
my.print()
my.Delete(1)
my.print()
my.Delete(1)
my.print()

console.log(my.Heapify([10,9,8,7,6,5,4]))
console.log(my.FindMin())
