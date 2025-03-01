import java.io.*

/*
    1. 키 순서대로 작은순부터 sorting (같은 키는 없음)
     - 한명을 뽑아 줄의 맨 앞에 세운다
     -> 자기 앞에 자기보다 키 큰 학생이 없다면 그냥 그 자리에 서고 끝
     -> 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다.
     => 이떄 A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.
 */
fun main() = with(File("10431_input.txt").bufferedReader()){
    val N = readLine().toInt()
    val results = mutableListOf<String>()

    repeat(N){
        val input = readLine().split(" ").map { it.toInt() }
        val caseNumber = input[0]
        val heights = input.subList(1, input.size) // 첫 번째 값을 제외한 배열

        var moves = 0
        val line = mutableListOf<Int>()

        // 줄서기 과정 (삽입 정렬 방식)
        for (height in heights) {
            print("height:: $height ")
            var position = line.size
            print("position: $position ")
            for (i in line.indices){
                if(line[i] > height) {
                    print("i:: $i ")
                    position = i
                    break
                }
            }

            // 밀려난 학생 수 = 뒤에 있는 학생 수
            moves += line.size - position
            line.add(position, height)
            println("moves:: $moves, line:: $line")
        }
        results.add("$caseNumber $moves")
    }

    println(results.joinToString("\n"))
}