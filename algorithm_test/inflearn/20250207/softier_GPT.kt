import java.io.*

fun main() = with(File("softier_GPT_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val strList = mutableListOf<Pair<Int, Int>>()
    repeat(N){
        val str = readLine()
        if('.' in str){
            val (f, s) = str.split(".")
            strList.add(Pair(first = f.toInt(), second = s.toInt()))
        } else {
            // strList.set(str.toInt(), 0)
            strList.add(Pair(first = str.toInt(), second = -1))
        }
        // println(strList)
    }

    val result = strList.sortedWith(compareBy<Pair<Int, Int>> {
        it.first
    }.thenBy {
        it.second
    })

    result.forEach{ it ->
        if(it.second == -1){
            println(it.first)
        } else {
            println("${it.first}.${it.second}")
        }
    }
    
}