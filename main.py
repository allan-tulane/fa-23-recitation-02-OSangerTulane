"""
CMPS 2200  Recitation 2
"""
import tabulate
import time


def simple_work_calc(n,a,b):
  if(n==1):
    return n
  else:
    return a*simple_work_calc(n//b,a,b)+n

def test_simple_work():
  assert simple_work_calc(8,2,2)==32
  assert simple_work_calc(8,3,2)==65
  assert simple_work_calc(9,2,3)==19
  assert simple_work_calc(10,3,2)==70
  assert simple_work_calc(8,4,2)==120
  assert simple_work_calc(12,4,3)==44

def work_cal(n,a,b,f):
    if(n==1):
        return n
    else:
        return a*work_cal(n//b,a,b,f)+f(n)

def test_work():
  assert work_cal(8,2,2,lambda n:n)==32
  assert work_cal(8,1,2,lambda n:n*n)==85
  assert work_cal(8,3,2,lambda n:1)==40
  assert work_cal(10,3,2,lambda n:n+2)==96
  assert work_cal(8,4,2,lambda n:n-1)==99
  assert work_cal(12,4,3,lambda n:n*5)==156

def compare_work(work_fn1,work_fn2,sizes=[10,20,50,100,1000,5000,10000]):
  result=[]
  for n in sizes:
    result.append((n,work_fn1(n),work_fn2(n)))
  return result

def print_results(results):
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))
  
def test_compare_work():
  work_fn1(1)==1
  work_fn2(1)==1
  work_fn1=lambda n:2*work_fn1(n//2)+work_fn1(n)
  work_fn2=lambda n:2*work_fn2(n//2)+work_fn2(n*n)
  res=compare_work(work_fn1,work_fn2)
  print_results(res)

def comapre_span(span_fn1,span_fn2,sizes=[10,20,50,100,1000,5000,10000]):
  result=[]
  for n in sizes:
    result.append((n,span_fn1(n),span_fn2(n)))
  return result
  
def span_calc(n,a,b,f):
  if(n==1):
    return n
  else:
    return a*span_calc(n//b,a,b,f)+f(n)
    
def test_compare_span():
  assert span_calc(10,2,2,lambda n:1)==15
  assert span_calc(20,1,4,lambda n:n*n)==426
  assert span_calc(30,3,4,lambda n:n)==60