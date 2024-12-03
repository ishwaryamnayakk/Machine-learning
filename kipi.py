{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "97017976",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number7\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def fib(n):\n",
    "    if n==1:\n",
    "        return 0\n",
    "    elif n==2:\n",
    "        return 1\n",
    "    else:\n",
    "        return fib(n-1)+fib(n-2)\n",
    "a=int(input(\"enter a number\"))\n",
    "fib(a)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "41249950",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "intList=[2,4,5]\n",
    "evenInts=filter(lambda x:x%2==0,intList)\n",
    "list(evenInts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0d5343b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 21, 81, 55, 26, 0, 34, 6, 62, 71, 76, 8, 38, 77, 78, 73, 14, 35, 61, 82]\n",
      "45.15 46.5\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "randomList=random.sample(range(0, 100), 20)\n",
    "print(randomList)\n",
    "from statistics import mean, median\n",
    "def getMeanAndMedian(listNum):\n",
    "    return mean(listNum), median(listNum)\n",
    "mean, median=getMeanAndMedian(randomList)\n",
    "print(mean,median)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9c6bc217",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee Details\n",
      "Name:kavya\n",
      "Total Salary:10000is total salary of all\n",
      "5000.0is average salary of all\n",
      "Name:ishu\n",
      "Total Salary:10000is total salary of all\n",
      "5000.0is average salary of all\n"
     ]
    }
   ],
   "source": [
    "employees=[\n",
    "    {\"name\":\"kavya\",\"salary\":5000},\n",
    "    {\"name\":\"ishu\",\"salary\":5000},\n",
    "]\n",
    "total_salary=sum(emp[\"salary\"]for emp in employees)\n",
    "average_salary=total_salary/len(employees)\n",
    "print(\"Employee Details\")\n",
    "for emp in employees:\n",
    "    print(f\"Name:{emp['name']}\")\n",
    "    print(f\"Total Salary:{total_salary}is total salary of all\")\n",
    "    print(f\"{average_salary}is average salary of all\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0a1416d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "matrix sum:\n",
      " [[ 6  8]\n",
      " [10 12]]\n",
      "matrix product:\n",
      " [[19 22]\n",
      " [43 50]]\n",
      "solution to AX=B: [0. 1.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "#define two matrices\n",
    "matrix1 = np.array([[1,2],[3,4]])\n",
    "matrix2 = np.array([[5,6],[7,8]])\n",
    "#matrix operations\n",
    "matrix_sum = matrix1 + matrix2\n",
    "matrix_product = np.dot(matrix1, matrix2)\n",
    "print(\"matrix sum:\\n\", matrix_sum)\n",
    "print(\"matrix product:\\n\",matrix_product)\n",
    "#solve a system of linear equations: Ax = B\n",
    "A = np.array([[3,1], [1,2]])\n",
    "B = np.array([1,2])\n",
    "solution = linalg.solve(A ,B)\n",
    "print(\"solution to AX=B:\", solution)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6bd74f2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54806a80",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
