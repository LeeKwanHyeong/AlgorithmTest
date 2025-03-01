import java.io.*
import kotlin.math.*
/*
    Baek 2579 계단 오르기

    1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.
*/

fun main() = with(File("2579_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val dp = Array(N+1){ 0 }
    val score = IntArray(N+1){ 0 }
    for (i in 1 until N+1) score[i] = readLine().toInt()

    dp[1] = score[1]
    if( N >= 2) dp[2] = score[1] + score[2]
    if (N >= 3) dp[3] = maxOf(score[1] + score[3], score[2] + score[3])

    for ( i in 4..N){
        dp[i] = maxOf(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
    }
    println(dp[N])
}