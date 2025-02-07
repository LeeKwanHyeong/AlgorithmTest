import java.io.*
import kotlin.math.*

fun main() = with(File("9095_input.txt").bufferedReader()){
    val T = readLine().toInt()
    val dp = Array(11){ 0 }

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for (i in 4..10){
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        println(dp.contentToString())
    }

    repeat(T){
        val n = readLine().toInt()
        println(dp[n])
    }
}