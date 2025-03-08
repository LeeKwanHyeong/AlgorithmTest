import java.io.*
import kotlin.math.*

/*
    [알리바바와 40인의 도둑] (bottom-up)
    알리바바는 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다.
    계곡의 돌다리는 NxN 돌들로 구성 (각 돌다리들은 높이가 서로 다름)
    -> 해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비. 이동은 최단거리로 이동.
    -> 즉, 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 한다.

    NxN 계곡의 돌다리 격자정보가 주어지면 (1, 1) 격자에서 (N, N)까지 가는데 드는 에너지의 최소량은?
*/

fun main() = with(File("inflearn_dp_7_input.txt").bufferedReader()){
    val N = readLine().toInt()

    val matrix = Array(N){ readLine().split(" ").map { it.toInt() }}
    var dp = Array(N){ Array(N){0} }
    matrix.forEach{ i -> println(i)}
    println()

    dp[0][0] = matrix[0][0]
    // 가장자리 다이나믹 값 
    for (i in 1 until N){
        dp[0][i] = dp[0][i-1] + matrix[0][i]
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    }

    for (i in 1 until N){
        for (j in 1 until N){        
                dp[i][j] = min(dp[i-1][j] + matrix[i][j], dp[i][j-1] + matrix[i][j])
        }
    }

    dp.forEach { i -> println(i.contentToString())}

    println(dp[N-1][N-1])


}