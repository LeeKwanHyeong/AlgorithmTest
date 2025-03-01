import java.io.*

fun main() = with(File("softier_CPTI_input.txt").bufferedReader()){
    val(N, M) = readLine().split(" ").map{ it.toInt() }
    val freqMap = mutableMapOf<Int, Int>()

    // 입력을 2진수 정수로 변환하여 Map에 저장
    repeat(N){
        val binary = readLine().toInt(2) // 2진수 변환
        freqMap[binary] = freqMap.getOrDefault(binary, 0) + 1
    }

    val keys = freqMap.keys.toList()
    var result = 0

    for ( i in keys.indices){
        for (j in i until keys.size){
            val diff = keys[i] xor keys[j]
            if(Integer.bitCount(diff) <= 2){
                result += freqMap[keys[i]]!! * freqMap[keys[j]]!!
                if(i == j) result -= freqMap[keys[i]]!!
            }
        }
    }

    println(result)

}