import java.io.File

fun main() {
    val list = List(6){it * it}
    
    /**
     * Collection 함수
     */
    // 추출
    println(list.slice(1..3))
    println(list.take(2))
    println(list.drop(2))
    println(list.takeWhile { it < 10 }) // 선택 후 추출
    println(list.dropWhile { it < 10 }) // 제거 후 추출

    // 집계 함수
    val list2 = (1..5).toList()
    println(list2.reduce { acc, n -> acc + n * 2}) // 누적 값 반환
    println(list2.fold(0){ acc, n -> acc + n * 2}) // 기초 값 기준으로 누적 값 반환

    // 필터
    val list3 = listOf("Red", "Green", "Blue")
    println(list3.filter { it.length > 3 })
    println(list3.filterNot { it.length > 3 })

    /*
     * 배열 
     */
    // 배열 쉽게 생성
    val arr1 = intArrayOf(1, 2, 3)
    val arr2 = IntArray(4){ 0 }
    val arr3 = IntArray(4){ it * 2 } // it == index

    print(arr3.contentToString())

    // 다차원 배열
    val n = 2
    val m = 3
    val arr4 = Array(n){
        BooleanArray(m)
    }
    arr4[0][0] = true
    println(arr4[0][0])

    // 리스트
    // 불변리스트
    val list4 = listOf(1, 2, 3)
    val list5 = mutableListOf(1, 2, 3)

    // 가번 리스트
    val list6 = List<Int>(5) { 0 }

    /*
     * Stack
     * 별도의 스택 클래스가 존재하지 않음. 
     */
    val stack = MutableList<Int>(4){ it } // 인덱스

    stack.add(5) // push
    stack.removeLast() // pop
    stack.last() // peek

    stack.isEmpty()
    stack.isNotEmpty()

    /* 
     * Queue
     * 큐 또한 따로 존재하지 않지만, LinkedList를 활용해서 비슷한 기능 기대
     */
    val q = LinkedList<Int>()
    q.offer(3) // Push
    q.peek() // peek
    q.poll() // pop

    /*
     * Deque
     * deque 자료구조 (덱, 디큐)를 활용해서 양방향 큐를 구현할 수 있다. 
     */
    val deque = ArrayDeque<Int>()

    deque.addLast(1)
    deque.add(2)
    println(deque)
    deque.addLast(4)
    println(deque)
    deque.add(5)
    println(deque)

    deque.removeFirst()
    deque.removeLast()

    deque.first()
    deque.last()
}