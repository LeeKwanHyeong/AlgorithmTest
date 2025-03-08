import java.io.*
import kotlin.collections.last

fun main() = with(File("input.txt").bufferedReader()){
    val N = readLine()!!.toInt()

    var result = BooleanArray(21){ false }
    lateinit var mode: String
    var x = 0
    val output = StringBuilder()

    repeat(N){
        val parts = readLine().split(" ")
        mode = parts[0]
        x = if(parts.size > 1)parts[1].toInt() else 0

        when(mode){
            "add" -> {
                if(!result[x]) result[x] = true
            }
            "remove" -> {
                if (result[x]) result[x] = false
            }
            "check" -> {
                if(result[x]==true) output.append("1\n")
                else output.append("0\n")
            }
            "toggle" -> {
                if(result[x] == true) result[x] = false
                else result[x] = true
            }
            "all" -> {
                result.fill(true)
            }
            "empty" -> {
                result.fill(false)
            }
        }
    }
    println(output)

}