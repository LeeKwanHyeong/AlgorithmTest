import java.io.*
import kotlin.math.*

fun main() = with(File("1463_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val dp = IntArray(N + 1) { 0 }

    for (i in 2..N) {
        dp[i] = dp[i - 1] + 1  // 기본: -1 연산
        if (i % 2 == 0) dp[i] = minOf(dp[i], dp[i / 2] + 1)  // 2로 나누기 가능
        if (i % 3 == 0) dp[i] = minOf(dp[i], dp[i / 3] + 1)  // 3으로 나누기 가능
        println(dp.contentToString())
    }

    println(dp[N])
}