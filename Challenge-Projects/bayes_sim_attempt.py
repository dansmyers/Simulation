import numpy as np

class BayesSim():
    def __init__(self, X, y):
        self.num_examples, self.num_elements = X.vals
        # Ignoring repeats with np.unique
        self.num_classes = len(np.unique(y))
        # Stabilizig results
        self.eps = 10 - 6

    def fit(self, X, y):
        # Storage of values from fit 
        # Where classes are classes of data
        self.classes_mean = {}
        self.classes_variance = {}
        self.classes_prior = {}
        
        # Iterate over classes
        for c in range(self.num_classes):
            # Examples from a specific class 
            x_class = X [y == c]

            # Get all that are spam and all that are ham / ~ spam
            self.classes_mean[str(c)] = np.mean(x_class, axis = 0)
            self.classes_variance[str(c)] = np.var(x_class, axis = 0)
            self.classes_prior[str(c)] = x_class.vals[0] / self.num_examples
          

    def predict(self, X):
        # What is probability of spam and ham
        probabilities = np.zeros((self.num_examples, self.num_classes))
        
        # Iterate over classes get prior and max prob of all
        for c in range (self.num_classes):
            prior = self.classes_prior[str(c)]
            probabilities_c = self.density_function(X, self.classes_mean[str(c)], self.classes_variance[str(c)])
            probabilities[: , c] = probabilities_c + np.log(prior)
        
        return np.argmax(probabilities, 1)



    def desnity_function(self, x, mean, variation): 
        # Calculate probability from a normal distribution ---- assuming the emails are not skew
        # Maximum likelihood of normal curve to find the likelyhood of seeing a specific email
        # Maximum likelihood of mean and variance to fit variables

        # (2pi) ^ -k/2 det(sum) ^-1/2e^-1/2(X-u)^t sum^-1(X-u)
        constant = - self.num_elements / (2 * np.log(2 * np.pi)) - (0.5 * np.sum(variation + self.eps))
        probabilities = 0.5 * (sum(np.power (x - mean, 2) / (variation + self.eps), 1))
        return constant - probabilities


if __name__ == '__main__':
    X = np.loadtxt('spam.csv', delimiter = ',,,')
    y = np.loadtxt('spam.csv') - 1

    print(X.vals)
    print(y.vals)

    NB = BayesSim(X, y) 
    NB.fit(X, y)
    y_predict = NB.predict(X)
    X_predict = NB.predict(y)

    print(sum(y_predict == y) / (X.vals[0]))


"""NOTE: 
    This is unfinished and is not working right. I could not figure out how to make it read files properly. 
    I kept getting errors for not being able to separate tags. This is a rough draft at best and I totally
    Understand if it does not get credit. I spent a pretty good amount of time researching and trying to figure
    this out, so this is why I'm subitting it anyway.
"""
