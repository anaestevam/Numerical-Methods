#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum
{
	BEZIER_RECURSIVA,
	BEZIER_NAORECURSIVA
};

// implemente uma das duas funções abaixo, mude a variável metodo para alternar o uso de uma ou de outra
// em ambas as funções, o parâmetro v contém ou só as abscissas dos pontos ou só as ordenadas
//  por exemplo, se os pontos são (0, 2), (3, 4) e (7, 5)
//  bezier será chamada com as abscissas, ou seja, com o vetor 0, 3, 7
//  e também será chamada com as ordenadas, ou seja, com o vetor 2, 4, 5

// mude essa variável para usar a função bezier1 (recursiva) ou bezier2 (não recursiva)
int metodo = BEZIER_RECURSIVA;

// implementacao recursiva (nao use memoization para comparar os tempos)
// retorna o ponto da curva bezier em t considerando os pontos Pa, ..., Pb
// essa função deve ficar consideravelmente lenta a partir de 8+ pontos
float bezier1(float *v, int a, int b, float t)
{
	return 0;
}

// implementacao nao recursiva
// retorna o ponto da curva bezier em t considerando os pontos P0, ..., Pn-1
// essa implementação deve ser mais eficiente que a recursiva sem memoization
float bezier2(float *v, int n, float t)
{
	memcpy() return 0;
}

int main()
{

	int n = 4;					// quantidade de pontos
	float vx[4] = {1, 3, 5, 7}; // abscissas
	float vy[4] = {1, 4, 3, 0}; // ordenadas

	for (float t = 0; t <= 1; t += 0.01)
	{
		if (metodo == BEZIER_RECURSIVA)
			printf("%f %f\n", bezier1(vx, 0, n - 1, t), bezier1(vy, 0, n - 1, t));
		else
			printf("%f %f\n", bezier2(vx, n, t), bezier2(vy, n, t));
	}

	return 0;
}