[toc]

# Pandas

pandas 사용법에 대해 정리합니다.

* pandas는 별칭 `pd`를 사용합니다.
* series는 별칭 `sr`을 사용합니다.
* dataframe은 별칭 `df`를 사용합니다.



## pd.Series()

pd.Series() : series객체를 생성합니다. `series객체는 한 행의 데이터`라고 할 수 있습니다.

다음과 같은 매개변수가 있습니다.

* `data` : 행 데이터의 집합, dict를 넘겨줄 경우 index도 할당됨
  * array-like, iterable, dict, scalar value
* `index` : value에 해당하는 이름의 집합. 중복 가능하다. 기본은 0부터 순서대로 할당된다.
  * array-like

* `dtype` : 데이터 타입을 지정한다. 숫자 이외의 데이터에는 `object`로 출력된다.

### series+비교연산자

series 객체에 비교 연산자를 사용하면, 객체내의 각각의 데이터와의 비교한 결과를 series 객체로 반환합니다.

* ex) pd.Series([1,2,3]) > 2	-> pd.Series([False, False, True])



## pd.DataFrame()

### df.loc

rows, columns의 그룹으로 접근합니다. label 또는 [`boolean array`](#series+비교연산자)로 접근 가능합니다.

* df.loc[행라벨]
* df.loc[[행라벨,행라벨]]
* df.loc[행라벨:행라벨]
* df.loc[:, 열라벨]
* df.loc[:, [열라벨, 열라벨]]
* df.loc[:, 열라벨:열라벨]