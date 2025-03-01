import java.io.*
import kotlin.collections.mapOf
import kotlin.collections.sortedMapOf
/*
    순위
    1. 금메달 수가 더 많은 나라
    2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
    3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

    문제: 어느 국가가 몇등 했는지 말하라.
    K 국가의 등수는?
 */
fun main() = with(File("8979_baek.txt").bufferedReader()) {
    val (N, K) = readLine().split(" ").map{ it.toInt() }
    var triple = Triple(0, 0, 0)
    val countries = mutableListOf<Triple<Int, Int, Int>>()

    repeat(N){
        val (id, gold, silver, bronze) = readLine().split(" ").map {it.toInt()}
        countries.add(Triple(gold, silver, bronze))
        if (id == K) triple = Triple(gold,silver,bronze)
    }

    countries.sortWith(compareBy<Triple<Int,Int,Int>>{ 
        it.first
    }.thenBy{
         it.second
    }.thenBy {
         it.third
    })

    countries.reverse()

    for (i in countries.indices){
        if (countries[i] == triple){
            println(i + 1)
            break
        }
    }

}