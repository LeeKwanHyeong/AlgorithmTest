/*
2024는 뭔가 특별하다..
T0(n)을 n의 약수이면서 홀수인 양의 정수인 개수
Te(n)을 n의 약수이면서 짝수인 양의 정수의 개수

Te(x) = K * T0(x)를 만족하는 양의 정수 x를 K-특별한 수

N: 양의 정수 K: 음이 아닌 정수


// 1, 2, 4, 5, 10, 20
// 홀수 2개 짝수 4개

4 = 2 * 2

문제: N 이하의 양의 정수 중 K-특별한 수의 개수
*/

import java.io.*
import kotlin.math.sqrt
import kotlin.math.sqrt

fun main() {
    val path = "input.txt"
    val reader = BufferedReader(FileReader(File(path)))

    val case = reader.readLine().toInt()
    val result = StringBuilder()
    val pow = LongArray(64)
    pow[0] = 1
    for (i in 1..63) {
        pow[i] = pow[i - 1] * 2
    }

    repeat(case) {
        val (N, K) = reader.readLine().split(" ").map { it.toLong() }

        var wcount = 0L

        if (K >= 63) {
            result.append(0).append("\n")
        } else {
            val tmp = K.toInt()
            val ans = N / pow[tmp]
            if (ans % 2 == 0L) {
                result.append(ans / 2).append('\n')
            } else {
                result.append(ans - (ans - 1) / 2).append('\n')
            }
        }
    }
    println(result)
}
