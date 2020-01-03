# PEP8 괄호 안 코드가 길 때

다음과 같이 코드가 길어 몇개의 줄로 나누어쓸 경우

```python
foo = long_function_name(var_one, var_two, var_three, var_four)
```



1. 첫 줄, 첫 파라미터에 맞추어 정렬한다.

   ```python
   foo = long_function_name(var_one, var_two,
                            var_three, var_four)
   ```

2. 둘째 줄에 첫 파라미터를 쓰고 해당 라인에서 한 단계 높은 들여쓰기를 한다.

   ```python
   foo = long_function_name(
       var_one, var_two,
       var_three, var_four)
   ```

   