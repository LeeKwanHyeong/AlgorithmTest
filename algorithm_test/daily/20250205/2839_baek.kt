import java.io.*

/*
    상근이는 사탕가게에 설탕을 정확하게 Nkg 배달해야 한다.
    설탕은 봉지에 담겨져 있다. 봉지는 3kg, 5kg 봉지가 있다.

    최대한 적은 봉지를 들고가려 한다.

    상근이가 설탕을 정확하게 Nkg 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 수를 구하라
*/

fun main() = with(File("2839_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val dp = IntArray(N + 1) { Int.MAX_VALUE }  // 초기화
    dp[0] = 0  // 0kg은 봉지 0개 필요

    for (i in 1..N) {
        println("i = $i")
        if (i >= 3 && dp[i - 3] != Int.MAX_VALUE) {
            dp[i] = minOf(dp[i], dp[i - 3] + 1)
        }
        if (i >= 5 && dp[i - 5] != Int.MAX_VALUE) {
            dp[i] = minOf(dp[i], dp[i - 5] + 1)
        }
        println(dp.contentToString())
    }

    println(if (dp[N] == Int.MAX_VALUE) -1 else dp[N])

}