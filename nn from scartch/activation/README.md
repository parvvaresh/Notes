1. **Sigmoid Function (Logistic Function)**:
   - Formula: $$\( \sigma(x) = \frac{1}{1 + e^{-x}} \)$$
   - Range: (0, 1)
   - Explanation: Sigmoid function squashes the input values between 0 and 1, making it useful for binary classification problems where you want to output probabilities.

2. **Hyperbolic Tangent Function (Tanh)**:
   - Formula: $$\( \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} \)$$
   - Range: (-1, 1)
   - Explanation: Tanh function is similar to the sigmoid function but squashes the input values between -1 and 1, making it zero-centered, which can help with the convergence of the neural network.

3. **Rectified Linear Unit (ReLU)**:
   - Formula: $$\( f(x) = \max(0, x) \)$$
   - Range: [0, +∞)
   - Explanation: ReLU function returns 0 for all negative input values and leaves positive values unchanged. It's widely used because of its simplicity and effectiveness in training deep neural networks.



4. **Softmax Function**:
   - Formula: $$\( \text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j}^{ } e^{x_j}} \)$$
   - Range: (0, 1) for each output, summing to 1 across all outputs.
   - Explanation: Softmax function is primarily used in the output layer of a neural network for multi-class classification problems. It converts raw scores into probabilities, allowing the model to predict the class with the highest probability.
  
5. The unit step function, also known as the Heaviside step function, is a mathematical function denoted as \( u(x) \) or \( H(x) \), which has a value of 0 for \( x < 0 \) and a value of 1 for \( x \geq 0 \). It essentially "turns on" at \( x = 0 \) and remains "on" for all values greater than or equal to 0. Mathematically, it can be defined as:

$$\[
u(x) = 
\begin{cases} 
0 & \text{if } x < 0 \\
1 & \text{if } x \geq 0 
\end{cases}
\]$$

In Python, you can implement the unit step function using a simple if-else statement or using numpy's `where()` function for vectorized operations. Here's how you can implement it using both methods:


```



These are some of the most commonly used activation functions in neural networks, each with its own characteristics and suitability for different types of problems.
