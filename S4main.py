#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt
from pathlib import Path

Path("images").mkdir(exist_ok=True)

# Loi de Dirac

x = np.array([3])
y = np.array([1])

plt.figure()
plt.stem(x, y)
plt.title("Loi de Dirac (x₀ = 3)")
plt.xlabel("x")
plt.ylabel("P(X = x)")
plt.tight_layout()
plt.savefig("images/Loi_dirac.png")
plt.close()

# Loi uniforme discète

from scipy.stats import randint

a = 1
b = 10
x = np.arange(a, b + 1)
y = randint.pmf(x, a, b + 1)

plt.figure()
plt.stem(x, y)
plt.title("Loi uniforme discrète {1,...,10}")
plt.xlabel("x")
plt.ylabel("P(X = x)")
plt.tight_layout()
plt.savefig("images/Loi_uniforme_discrète.png")
plt.close()

# Loi binomiale

from scipy.stats import binom

n = 20
p = 0.4
x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)

plt.figure()
plt.stem(x, y)
plt.title("Loi binomiale (n=20, p=0.4)")
plt.xlabel("x")
plt.ylabel("P(X = x)")
plt.tight_layout()
plt.savefig("images/Loi_binomiale.png")
plt.close()

# Loi de Poisson

from scipy.stats import poisson

mu = 5
x = np.arange(0, 20)
y = poisson.pmf(x, mu)

plt.figure()
plt.stem(x, y)
plt.title("Loi de Poisson(µ = 5)")
plt.xlabel("x")
plt.ylabel("P(X = x)")
plt.tight_layout()
plt.savefig("images/Loi_poisson.png")
plt.close()

# Loi de Zipf-Mandelbrot

k = np.arange(1, 50)
s = 1.5
q = 1

y = 1 / (k + q) ** s
y = y / y.sum()

plt.figure()
plt.stem(k, y)
plt.title("Loi de Zipf-Mandelbrot")
plt.xlabel("k")
plt.ylabel("P(X = x)")
plt.tight_layout()
plt.savefig("images/Loi_ZipfMandelbrot.png")
plt.close()


# loi normale

x = np.linspace (-4, 4, 1000)
y = scipy.stats.norm.pdf(x)

plt.plot(x,y)
plt.title("Loi normale")
plt.xlabel("x")
plt.ylabel("Densité de probabilité")
plt.tight_layout()
plt.savefig("images/Loi_normale.png")
plt.close()

# Loi log-normale
from scipy.stats import lognorm

x = np.linspace(0, 5, 1000)
sigma = 0.5
y = lognorm.pdf(x, s=sigma)

plt.figure()
plt.plot(x, y)
plt.title("Loi log-normale (σ = 0.5)")
plt.xlabel("x")
plt.ylabel("densité")
plt.tight_layout()
plt.savefig("images/Loi_log_normale.png")
plt.close()


# Loi uniforme 

from scipy.stats import uniform

a = 0
b = 10
x = np.linspace(a, b, 1000)

y = uniform.pdf(x, loc=a, scale=b-a)

plt.figure()
plt.plot(x, y)
plt.title("Loi uniforme U(0,10)")
plt.xlabel("x")
plt.ylabel("densité")
plt.tight_layout()
plt.savefig("images/Loi_uniforme.png")
plt.close()

# Loi du khi-deux

from scipy.stats import chi2

k = 4
x = np.linspace(0, 20, 1000)
y = chi2.pdf(x, df=k)

plt.figure()
plt.plot(x, y)
plt.title("Loi du χ² (k = 4)")
plt.xlabel("x")
plt.ylabel("densité")
plt.tight_layout()
plt.savefig("images/Loi_chi2.png")
plt.close()

# Loi de Pareto

from scipy.stats import pareto

x = np.linspace(1, 10, 1000)
b = 3
y = pareto.pdf(x,b)

plt.figure()
plt.plot(x, y)
plt.title("Loi de Pareto (b = 3)")
plt.xlabel("x")
plt.ylabel("densité")
plt.tight_layout()
plt.savefig("images/Loi_pareto.png")
plt.close()

#https://docs.scipy.org/doc/scipy/reference/stats.html


dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)


# Moyennes et écart-type

def moyenne_discrete(x, p): 
    return np.sum(x * p)

def ecart_type_discrete(x, p):
    mu = moyenne_discrete(x, p)
    return np.sqrt(np.sum((x - mu)**2 * p))

def moyenne_continue(x, f):
    dx = x[1] - x[0]
    return np.sum(x * f) * dx

def ecart_type_continue(x, f):
    mu = moyenne_continue(x, f)
    dx = x[1] - x[0]
    return np.sqrt(np.sum((x - mu)**2 * f) * dx)

# Exemple : Loi de Poisson
from scipy.stats import poisson

x = np.arange(0, 20)
p = poisson.pmf(x, mu=5)

print("Poisson")
print("Moyenne :", moyenne_discrete(x, p))
print("Ecart-type :", ecart_type_discrete(x, p))

    
