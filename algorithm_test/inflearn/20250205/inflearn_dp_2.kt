import java.io.*

fun main() = with(File("inflearn_dp_2_input.txt").bufferedReader()){
    val N = readLine().toInt()

    val dp = IntArray(N + 1){ 0 }

    fun DFS(len: Int): Int{
        when {
            dp[len] > 0 -> return dp[len]
            len == 1 || len == 2 -> return len
            else -> {
                dp[len] = DFS(len - 1) + DFS(len - 2)
                return dp[len]
            }
        }
    }

    println(DFS(N))

}