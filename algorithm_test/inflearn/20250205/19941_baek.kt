import java.io.*

/*
    백준 21921: [햄버거 분배]
    기다란 벤치 모양의 식탁에 사람들과 햄버거가 1단위 간격으로 놓여 있다. 
    사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.
    N: 식탁의 길이
    K: 햄버거를 선택할 수 있는 거리
    햄버거 위치
*/

fun main() = with(File("19941_input.txt").bufferedReader()){
    val (N, K) = readLine().split(" ").map{ it.toInt() }
    val strTable = readLine().toMutableList()
    var result = 0

    he@
    for (index in strTable.indices){
        if(strTable[index] == 'P'){
            for (i in K downTo 1){
                if (index - i >= 0 && strTable[index - i] == 'H'){
                    result++
                    strTable[index - i ] = 'K'
                    continue@he
                }
            }
            for (i in 0..K){
                if(index + i < strTable.size && strTable[index + i] == 'H' ){
                    result++
                    strTable[index + i] = 'K'
                    continue@he
                }
            }
        }
    }
    
    println(result)

    
}