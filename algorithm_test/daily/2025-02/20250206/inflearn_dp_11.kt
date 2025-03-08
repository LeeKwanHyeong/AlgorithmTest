import java.io.*
import kotlin.math.*

/*
    최대점수 구하기(냅색 알고리즘)
    선생님이 주신 N개의 문제를 풀려고 한다.
    그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어진다.
    N: 문제 개수 M: 제한 시간
    S: 점수 T: 푸는데 걸리는 시간

    이차원 배열로 필요하다. 한 문제만 풀 수 있기 때문에...
*/

fun main() = with(File("inflearn_dp_11_input.txt").bufferedReader()){
    val (N, M) = readLine().split(" ").map{ it.toInt() }
    val dp = IntArray(M + 1){ 0 }
    println(dp.contentToString())

    repeat(N){
        val (S, T) = readLine().split(" ").map { it.toInt() }
        for (i in M downTo T){
            dp[i] = max(dp[i - T] + S, dp[i])
        }
        println(dp.contentToString())
    }

    // repeat(N){
    //     val (S, T) = readLine().split(" ").map{ it.toInt() }
    //     for (i in T until M+1){
    //         dp[i] = max(dp[i], dp[i - T] + S)
    //     }
    //     println(dp.contentToString())
    // }

}