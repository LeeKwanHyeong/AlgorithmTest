import java.io.*

/*
    A의 몸무게, 키 = X, Y
    B의 몸무게, 키 = P, Q
    A가 B의 몸무게와 키보다 크면 A가 B보다 덩치가 크다.

    만약
    C의 몸무게, 키 = 45, 181
    D의 몸무게, 키 = 55, 173
    몸무게는 D가 C보다 더 무겁고, 키는 C가 더 크므로, '덩치'로만 볼때 C와 D는 누구도 
    상대방보다 더 크다고 할 수 없다.
*/

fun main() = with(File("7568_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val people = mutableListOf<Pair<Int, Int>> ()

    repeat(N) {
        val (weight, height) = readLine().split(" ").map { it.toInt() }
        people.add(Pair(weight, height))
    }

    val ranks = IntArray(N) { 1 }

    for (i in 0 until N){
        for (j in 0 until N){
            if (i == j) continue // 자기 자신은 비교하지 않음

            // i번째 사람이 j번째 사람보다 덩치가 작으면 등수 증가
            if(people[i].first < people[j].first && people[i].second < people[j].second){
                ranks[i]++
            }
        }
    }

    println(ranks.joinToString(" "))
}