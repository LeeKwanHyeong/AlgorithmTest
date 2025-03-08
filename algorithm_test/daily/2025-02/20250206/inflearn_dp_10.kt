import java.io.*
import kotlin.math.*
/*
    동전 교환 [냅색 알고리즘]
    여러 단위의 동전들이 주어져있을때, 거스름돈을 가장 적은 수의 동전으로 교환해주려면?
*/

fun main() = with(File("inflearn_dp_10_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val K = readLine().split(" ").map{ it.toInt() }
    val remain = readLine().toInt()
    val dp = IntArray(remain+1){ 1000 }
    dp[0] = 0

    for ( i in K){
        for (j in i until remain+1){
            dp[j] = min(dp[j], dp[j-i] + 1)
            println(dp.contentToString())
        }
    }

    println(dp.last())

}