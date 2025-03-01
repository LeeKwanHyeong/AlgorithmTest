import java.io.*
import kotlin.math.*

/*
    [가방문제] 냅색알고리즘
    최고 17kg의 무게를 저장할 수 있는 가방이 있다.
    3kg, 4gk, 7kg, 8kg, 9kg의 무게를 가진 5종류의 보석이 있다. 각 보석의 가치는 4, 5, 10, 11, 13.

*/

fun main() = with(File("inflearn_dp_9_input.txt").bufferedReader()){
    val(n, max) = readLine().split(" ").map{ it.toInt() }
    var dp = IntArray(max + 1){ 0 }

    repeat(n){
        val( w, v ) = readLine().split(" ").map { it.toInt() }
        for (i in w until max+1){
            dp[i] = max(dp[i], dp[i-w] + v)
        }
    }
    println(dp.max())
}