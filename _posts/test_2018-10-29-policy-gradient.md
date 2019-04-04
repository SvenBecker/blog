---
title: Policy Gradient Algorithms
date: 2018-10-23
header:
    overlay_image: https://images.unsplash.com/photo-1528819622765-d6bcf132f793?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8cf14450e7ab6e30d85800342f9ed485&auto=format&fit=crop&w=1500&q=80
    teaser: https://images.unsplash.com/photo-1528819622765-d6bcf132f793?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8cf14450e7ab6e30d85800342f9ed485&auto=format&fit=crop&w=1500&q=80
    og_image: https://images.unsplash.com/photo-1528819622765-d6bcf132f793?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8cf14450e7ab6e30d85800342f9ed485&auto=format&fit=crop&w=1500&q=80
    overlay_filter: 0.7
excerpt: "An Introduction to Policy Gradient Algorithms"
categories:
    - Deep Learning
    - Academic
tags:
    - Policy Gradient
    - Reinforcement Learning
---

**Notice!** This page is still in progress!
{: .notice--primary}

# Policy Gradient Algorithms

*Proximal Policy Algorithms* (PPO) are a field of reinforcement learning algorithms where the object is to identify a agent policy, meaning
a function which maps the *optimal* behavior of an agent in an environment.

## The Log-Likelihood Trick

$$
\begin{aligned}
\nabla_\theta \mathbb{E}[R_t|\theta] &= \nabla_\theta \sum_{a \in \mathit{A}} \pi_{\theta}(a) \mathbb{E}[R_t|A_t=a] \\
&= \sum_{a \in \mathit{A}} q(a) \nabla_\theta \pi_{\theta}(a) \\
&= \sum_{a \in \mathit{A}} q(a) \frac{\pi_{\theta}(a)}{\pi_{\theta}(a)} \nabla_\theta \pi_{\theta}(a) \\
&= \sum_{a \in \mathit{A}} \pi_{\theta}(a) q(a) \frac{\nabla_\theta \pi_{\theta}(a)}{\pi_{\theta}(a)} \\
&= \mathbb{E}[R_t \frac{\nabla_\theta \pi_{\theta}(A_t)}{\pi_{\theta}(A_t)}] \\
&= \mathbb{E}[R_t \nabla_\theta \log \pi_{\theta}(A_t)]
\end{aligned}
$$

## Baseline

The policy gradient algorithm nowadays will most of the time include a so called baseline $b$. The baseline has the purpose to achieve a smoother convertion of the agents policy by reducing the parameter update size. Assuming we perform gradient ascent, the update of $\theta$ can be formulated as follows:
$$
\theta = \theta + \alpha (R_t - b) \nabla_{\theta} \log \pi_{\theta}(A_t).
$$
In this notation the reward $R_t$ will be reduced by some baseline $b$ which will lead to a smaller policy update.

**Why does that work?**

It seems counter intuitive to be allowed to simply add some constant or variable to the policy update function. If we sum up all action probabilities this will result in $\sum_{a} \pi_{\theta}(a) = 1$, thus we can guarantee for all $b$ which are neither dependent on $\theta$ nor $a$
$$
\begin{aligned}
\sum_{a}b \nabla_{\theta} \pi_{\theta}(a) &= \nabla_{\theta} \sum_{a} b \pi_{\theta}(a) \\
&= \nabla_{\theta} b \\
&= 0.
\end{aligned}
$$

> Baselines do not change the expected update, but they do change variance.
>
> DeepMind: Reinforcement-Learning Lesson 2 - Exploration and Exploitation

**How do I select a good baseline?**

There are multiple ways to select a descent baseline. The easiest way is to estimate the average reward given by
$$
b=\frac{1}{t}\sum_{i=1}^{t}R_{i}.
$$

A more common approach is to use a state dependent baseline $b(s_t)$ and in this context it is very pleasent that we already have a notation for such a baseline which is the value function $v_{\pi}(s_t)$. This gives us the so called *actor-ciritc* *algorithm*.

## Actor-Critic

![](https://www.kdnuggets.com/images/reinforcement-learning-fig4-552.jpg)

## References

- Richard S. Sutton and Andrew G. Barto: [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf), 2017.
- [TRPO paper](https://arxiv.org/abs/1502.05477)