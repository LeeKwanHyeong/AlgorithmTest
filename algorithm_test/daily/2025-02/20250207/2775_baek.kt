import java.io.*
import kotlin.math.*

/*
    Baek 2775 부녀회장이 될테야
    1. a층 b호에 살려면 자신의 아래 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼
    사람들을 데려와 살아야 한다.file

    2. 아파트에 비어있는 집은없고 모든 거주민들이 이 계약 조건을 지키고 왔다.

    양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력.
*/

fun main() = with(File("2775_input.txt").bufferedReader()){
    val T = readLine().toInt()

    val apart = Array(15){ IntArray(15){ 0 } }
    for(i in 1 until 15){
        apart[0][i] = i
    }
    /*
        1층 1호 = 0층 1호
        1층 2호 = 0층 1호 + 0층 2호
        1층 3호 = 0층 1호 + 0층 2호 + 0층 3호 = 1층 2호 + 0층 3호
    */
    for (i in 1 until 15){
        for (j in 1 until 15){
            apart[i][j] = apart[i][j-1] + apart[i-1][j]
        }
    }

    repeat(T){
        val k = readLine().toInt()
        val n = readLine().toInt()

        println(apart[k][n])
    }
}