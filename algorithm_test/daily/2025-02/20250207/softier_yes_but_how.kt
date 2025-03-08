import java.util.*
import java.io.*

fun main() = with(File("softier_yes_but_how_input.txt").bufferedReader()){
    val arr = readLine()!!.trim().toList()
    val stack = mutableListOf<Int>()        // Stack 대신 MutableList 사용
    val result = mutableListOf<Char>()

    for (char in arr) {
        when (char) {
            '(' -> {
                result.add('(')
                stack.add(result.size - 1) // 여는 괄호 위치 추가
            }
            ')' -> {
                if (stack.isNotEmpty()) {
                    val idx = stack.removeAt(stack.size - 1) // 마지막 원소 가져오기
                    if (idx + 1 >= result.size || result[idx + 1] != '1') {
                        result.add('1')
                    }
                }
                result.add(')')
                result.add('+')
            }
        }
    }

    if (result.isNotEmpty()) result.removeAt(result.lastIndex) // 마지막 '+' 제거

    println(result.joinToString(""))
}