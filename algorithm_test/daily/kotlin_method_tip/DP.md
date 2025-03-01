# 🧠 Dynamic Programming (DP) 개념 및 Kotlin 활용 팁

---

## 📋 **1️⃣ DP란 무엇인가?**

### ✅ **정의:**
- **Dynamic Programming (DP)**는 **복잡한 문제를 더 작은 하위 문제로 나누어** 해결하는 알고리즘 기법입니다.
- **중복되는 부분 문제**를 효율적으로 처리하여 시간 복잡도를 줄입니다.

### 🎯 **DP의 핵심 요소:**
1. **Overlapping Subproblems (중복되는 부분 문제)**
   - 큰 문제를 해결하기 위해 동일한 작은 문제를 반복적으로 풉니다.
2. **Optimal Substructure (최적 부분 구조)**
   - 문제의 최적 해답이 **하위 문제의 최적 해답으로부터 구성**될 수 있습니다.

---

## 🚀 **2️⃣ DP 문제 해결 단계**

1. **문제 분석:**
   - 문제를 더 작은 하위 문제로 나눌 수 있는지 확인합니다.

2. **DP 테이블 정의:**
   - `dp[i]` 또는 `dp[i][j]` 형태로 하위 문제의 결과를 저장할 배열을 만듭니다.

3. **점화식 (Recurrence Relation) 도출:**
   - 현재 문제를 **이전 문제들의 결과를 기반으로** 정의합니다.

4. **초기값 설정 (Base Case):**
   - 가장 작은 하위 문제의 결과를 초기화합니다.

5. **Bottom-up 또는 Top-down 방식으로 구현:**
   - **Bottom-up (반복문)**: 작은 문제부터 해결하며 `dp` 배열에 결과를 저장합니다.
   - **Top-down (재귀 + 메모이제이션)**: 재귀 호출을 사용하면서 결과를 `dp` 배열에 저장하여 중복 계산 방지합니다.

---

## 💡 **3️⃣ DP 유형별 예제**

### ✅ **1. 피보나치 수열 (Top-down)**

```kotlin
fun fibonacci(n: Int, memo: IntArray): Int {
    if (n <= 1) return n
    if (memo[n] != -1) return memo[n] // 메모이제이션

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
}

fun main() {
    val n = 10
    val memo = IntArray(n + 1) { -1 } // 초기화
    println(fibonacci(n, memo))
}
```

### ✅ **2. 피보나치 수열 (Bottom-up)**

```kotlin
fun fibonacciBottomUp(n: Int): Int {
    val dp = IntArray(n + 1)
    dp[0] = 0
    dp[1] = 1

    for (i in 2..n) {
        dp[i] = dp[i - 1] + dp[i - 2]
    }
    return dp[n]
}

fun main() {
    val n = 10
    println(fibonacciBottomUp(n))
}
```

---

## 🚀 **4️⃣ Kotlin에서의 DP 구현 팁**

### 🔑 **1. `MutableList`와 `Array` 활용**
- **배열 (Array):** 고정된 크기의 데이터 처리에 효율적
- **가변 리스트 (MutableList):** 크기가 유동적인 경우 유용

```kotlin
val dp = Array(100) { IntArray(100) { -1 } } // 2차원 DP 배열 초기화
```

### 🔑 **2. `getOrPut`를 활용한 메모이제이션**
- `Map`을 이용한 메모이제이션으로 불필요한 계산 방지

```kotlin
val memo = mutableMapOf<Int, Int>()

fun fib(n: Int): Int = memo.getOrPut(n) {
    if (n <= 1) n else fib(n - 1) + fib(n - 2)
}

fun main() {
    println(fib(10))
}
```

### 🔑 **3. `minOf`, `maxOf`로 간결한 비교 처리**
- 최소값 또는 최대값을 구하는 로직을 간결하게 작성 가능

```kotlin
val minFuel = minOf(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
```

### 🔑 **4. `with` 블록으로 I/O 최적화**
- `BufferedReader`로 빠른 입력 처리

```kotlin
fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val dp = IntArray(n + 1)
    // DP 로직
}
```

---

## 📊 **5️⃣ DP의 시간 복잡도**

- **Bottom-up:** `O(N)` 또는 `O(N²)` (이중 반복문)
- **Top-down (메모이제이션):** `O(N)` (중복 호출 방지)

### **공간 복잡도 최적화:**
- 이전 결과만 필요하면 배열 대신 변수로 공간 절약 가능

```kotlin
fun fibonacciOptimized(n: Int): Int {
    var a = 0
    var b = 1
    repeat(n) {
        val temp = a + b
        a = b
        b = temp
    }
    return a
}
```

---

## 🎯 **6️⃣ 실전 DP 문제 추천**

1. **백준 1003 - 피보나치 함수**
2. **백준 1149 - RGB 거리**
3. **백준 1912 - 연속합**
4. **백준 1463 - 1로 만들기**
5. **백준 2579 - 계단 오르기**

---

## 🚀 **7️⃣ 핵심 요약**

| ✅ 핵심 개념          | 💡 설명                           |
|----------------------|----------------------------------|
| **부분 문제 중복**       | 동일한 작은 문제 반복 해결               |
| **최적 부분 구조**       | 큰 문제의 최적 해답 = 작은 문제의 최적 해답 |
| **Bottom-up 방식**      | 반복문으로 하위 문제부터 해결             |
| **Top-down + 메모이제이션** | 재귀 + 결과 저장으로 중복 호출 방지         |
| **Kotlin 특성 활용**     | `getOrPut`, `minOf`, `MutableList` 활용    |

---

💡 **DP는 연습이 중요합니다! 작은 문제부터 차근차근 해결하며 익숙해지세요. 🚀**

