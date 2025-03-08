import java.io.*
import kotlin.math.*

fun main() = with(File("inflearn_dp_4_input.txt").bufferedReader()){
    val N = readLine().toInt()
    var dp = IntArray(N + 1){ 0 }
    var arr = readLine().split(" ").map{ it.toInt() }.toMutableList()
    arr.add(0, 0)
    
    var  res = 0

    // 가장 긴 수열의 길이만
    dp[1] = 1

    for(i in 2 until N + 1){
        var max = 0
        for (j in i-1 downTo 1){
            if(arr[j] < arr[i] && dp[j] > max){
                max = dp[j]
            }
        }
        dp[i] = max + 1
        res = max(res, dp[i])
    }

    print(res)
}