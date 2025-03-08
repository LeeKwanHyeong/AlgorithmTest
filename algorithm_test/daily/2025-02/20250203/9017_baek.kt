import java.io.*
/*
    경주 코스 4 ~ 12km / 개인 성적을 통해 팀의 점수 계산
    한 팀: 6명 / 팀 점수: 상위 4명 점수 합
    우승: 점수를 더하여 가장 낮은 점수를 얻는 팀
    * 6명의 주자가 참가하지 못하면 점수 계산에서 제외
    * 동점인 경우 다섯 번째 주자가 가장 빨리 들어온 팀이 우승

*/

fun main() = with(File("9017_input.txt").bufferedReader()){
    val T = readLine().toInt()

    repeat(T){
        val N = readLine().toInt()
        val teamsList = readLine().split(" ").map{ it.toInt() }
        val eligibleList = mutableListOf<Int>()
        val resetList = mutableListOf<Int>()
        val result = mutableListOf<Pair<Int, MutableList<Int>>>()

        for (i in 1..N){
            val test = teamsList.count { it == i }
            if(test == 6){
                eligibleList.add(i)
            }
        }

        for (j in teamsList.indices){
            for (i in eligibleList){
                if (teamsList[j] == i) resetList.add(i)
            }
        }
        
        val eligibleMap = mutableMapOf<Int, MutableList<Int>>()
        resetList.forEachIndexed{ index, team -> 
            eligibleMap.getOrPut(team){ mutableListOf() }.add(index + 1)
        }

        val teamScores = eligibleMap.map { (team: Int, scores: MutableList<Int>) -> 
            val top4Sum = scores.take(4).sum()
            val fifthScore = scores[4]
            Triple(team, top4Sum, fifthScore)
        }

        val winner = teamScores.minWith(compareBy({it.second}, {it.third}))!!.first

        println(winner)

        
    }
}