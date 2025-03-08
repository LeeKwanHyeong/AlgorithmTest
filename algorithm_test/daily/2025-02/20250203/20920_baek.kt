import java.io.*
/*
    백준20920: [영단어 암기는 괴로워]
    단어장의 단어 순서는 다음과 같은 우선순위
    1. 자주 나오는 단어일수록 앞에 배치
    2. 단어의 길이가 길수록 앞에 배치
    3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치

*/

fun main() = with(File("20920_input.txt").bufferedReader()){
    val (N, M) = readLine().split(" ").map{ it.toInt() }

    // getOrPut
    val dictMap = mutableMapOf<String,Int>()
    val result = StringBuilder()

    repeat(N){
        val word = readLine()
        if (word.length >= M){
            dictMap[word] = dictMap.getOrPut(word){ 0 } + 1
        }
    }

    dictMap.toList()
        .sortedWith(compareByDescending<Pair<String, Int>>{
            it.second
        }.thenByDescending {
            it.first.length
        }.thenBy {
            it.first
        }).toMap(LinkedHashMap())
        .forEach { result.append(it.key).append('\n')}
    
    println(result)

}