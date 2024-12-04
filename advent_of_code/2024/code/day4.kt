fun puzzleInput(): String{
    val data = """HIDDEN"""
    return data
}

fun main(){
    val data = puzzleInput()
    val ary = data.split("\n").toTypedArray()

    // part 1
    // part 1a preparing the data
    val size = ary.size + 6
    val charAryIntermediate = Array<String>(size) {"_"}
    for (i in 0..2){
        charAryIntermediate[i] = ".".repeat(ary[0].length + 6)
    }
    for (i in 0..<ary.size){
        charAryIntermediate[i+3] = "..." + ary[i] + "..."
    }
    for (i in ary.size+3..ary.size+5){
        charAryIntermediate[i] = ".".repeat(ary[0].length + 6)
    }
    val charAry = Array(size) { Array<String>(size) {"_"} }
    for (i in 0..<charAryIntermediate.size){
        var chunked = charAryIntermediate[i].chunked(1)
        for (j in 0..<chunked.size){
            charAry[i][j] = chunked[j]
        }
    }

    // part 1b iterate thru the data and check for possibilities
    var answerP1 = 0
    for (i in 0..<charAry.size){
        for (j in 0..<charAry.size){
            if (charAry[i][j] == "X"){
                if(charAry[i-1][j] == "M" && charAry[i-2][j] == "A" && charAry[i-3][j] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i-1][j-1] == "M" && charAry[i-2][j-2] == "A" && charAry[i-3][j-3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i][j-1] == "M" && charAry[i][j-2] == "A" && charAry[i][j-3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i+1][j-1] == "M" && charAry[i+2][j-2] == "A" && charAry[i+3][j-3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i+1][j] == "M" && charAry[i+2][j] == "A" && charAry[i+3][j] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i+1][j+1] == "M" && charAry[i+2][j+2] == "A" && charAry[i+3][j+3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i][j+1] == "M" && charAry[i][j+2] == "A" && charAry[i][j+3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i-1][j+1] == "M" && charAry[i-2][j+2] == "A" && charAry[i-3][j+3] == "S"){answerP1 = answerP1 + 1}
            }
        }
    }
    println("Part 1 answer: $answerP1")

    // part 2 note that every cross mas has to begin with a A
    // iterate and possibilities
    var answerP2 = 0
    for (i in 0..<charAry.size){
        for (j in 0..<charAry.size){
            if (charAry[i][j] == "A"){
                var forwardSlash = charAry[i-1][j-1] + charAry[i+1][j+1]
                var backwardSlash = charAry[i-1][j+1] + charAry[i+1][j-1]
                if (
                    (forwardSlash == "SM" || forwardSlash == "MS") &&
                    (backwardSlash == "SM" || backwardSlash == "MS")
                ){answerP2 = answerP2 + 1}
            }
        }
    }
    println("Part 2 answer: $answerP2")
}