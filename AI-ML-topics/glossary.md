* Accuracy (classification): A measure which is defined as the number of correct predictions divided by the total number of predictions.
* Anomaly Detection: Detecting data points that do not align with a recognized pattern across a set of data points.
* Area Under the Curve: the percentage of area underneath the ROC curve. This is a measure of how accurate the two-class model is, with numbers closer to 1 being better.
* API: Application programming interfaces that are exposed to help multiple applications and systems interact with each other.
* Artificial Intelligence: the ability for a computer to simulate human cognitive behavior.
* Autonomous: An autonomous system is a system that can accomplish a task without human involvement during the execution of the task.
* Azure Cognitive Services: A suite of AI Services targeting specialized AI workloads to help developers implement AI capabilities into their solution with minimal AI and ML expertise.
* Azure Machine Learning: A cloud-based service that delivers a platform supporting the creation and deployment of Machine Learning Models.
* Azure Machine Learning Studio: The integrated development environment (IDE) for Azure Machine Learning.
* Compute (Azure ML): Virtual machine resources which are dedicated to performing tasks in Azure Machine Learning. Compute may include individual virtual machines (VMs), typically configured as data science VMs, or it may include a cluster of VMs intended for training and inference pipeline executions.
* Computer Vision: A domain of artificial intelligence focused on processing and understanding visual inputs through complex machine learning algorithms. 
* Computer vision: the process of interpreting the world visually. We train models on videos or images, typically to recognize some object, state, or interaction. 
* Confusion matrix: A table representing predicted versus actual values for a classification problem. A classic two-class confusion matrix has four boxes. Using "Yes" and "No" as the two classes, these four boxes are:
        True Positive: we predicted Yes correctly
        False Positive: we predicted Yes but it was really No
        False Negative: we predicted No but it was really Yes
        True Negative: we predicted No correctly
* Data Labeling: This functionality allows you to label images as part of an image classification project.
* Dataset: A dataset is a collection of data that is used to train the machine during the AI and ML processes.
* Differential privacy: A technique in which individual data points are modified with some constant error term. The end result is that the data points can no longer be tied back to specific locations but the distribution of this data remains the same in aggregate. For example, a dataset of police incidents may use differential privacy to protect accidental disclosure of information, such as knowledge of a domestic disturbance. The dataset would have each point (in latitude and longitude) enclosed in a circle of radius r, where r might be approximately one city block. We choose a random point within the circle and define that point as the location of the incident. On net, we know how many crimes there are in a particular neighborhood, but we do not necessarily know at which houses the incidents occur.
* Experiment: In the context of AI and ML, experiment refers to using the AI and ML processes to see if a particular question can be answered with AI and ML, or a hypothesis can be supported or validated.
* Experiment (Azure ML): A collection of trials used to validate a user's hypothesis. An experiment may contain multiple runs of pipelines.
* Feature: Inputs which help us understand what affects the label.
* Feature engineering: Creating new features from existing data. This might include calculating new features, translating a street address into latitude and longitude, or parsing passages of text for meaning.
* Feature selection: Removing a column from consideration when training a model.
* Go: An abstract strategy-based board game.
* Homomorphic encryption: A style of encryption which allows a developer or data scientist to perform calculations on encrypted data without decrypting it first. The result of these calculations will also be in an encrypted form and the decrypted result will be exactly the same as if we performed all of the operations on unencrypted data. This ensures that data scientists can work on data sets while maintaining maximum privacy, as they will not see the unencrypted data at any time.
* Intent: An intent represents the action the user wants to execute. It usually refers to a preferred action when a user delivers a sentence to be interpreted by the machine.
* Jupyter Notebook: A virtual notebook environment where developers can write notes and combine live code and visualizations into a single document.
* Knowledge mining: the process of extracting knowledge from vast amounts of information. In Azure, Azure Cognitive Search is the primary tool. It tags information in documents, allowing for easy, detailed searches of those documents.
* Label: The thing we want to predict.
* Linked Services: This functionality allows you to integrate Azure Machine Learning with other Azure services. At present, the only linked service offering is to connect to Azure Synapse Analytics, which is a modern data warehousing offering on Azure.
* Machine Learning Model: A machine learning model is a logic that has been trained to recognize certain types of patterns.
* Machine Learning Operations (MLOps): The practice involves the automation of processes required to build and deliver end-to-end Machine Learning Models and experiences.
* Mean Absolute Error (MAE): An evaluation measure for any regression model. It is the average difference between predicted and actual values. This works well when dealing with small ranges of numbers.
* Mean Absolute Percent Error (MAPE): An evaluation measure for any regression model. It is the percentage difference between the predicted and actual values. If the actual value is 0, MAPE will fail with a divide by 0 error, so it is not a good measure if the actual value can be 0. MAPE works best when you have large ranges of numbers.
* Microservice: A lightweight, independent service. Typically, microservices have one job and communicate with each other using well-defined operations.
* Natural Language Processing: A domain of artificial intelligence focused on understanding human language and helping computers and humans interact through human language.
* Natural language processing (NLP) is the process of interpreting written or spoken language. We train models based on written documents or audio clips of speech. 
* Node (input, output): An input or output connection point on a component. Each component will have 0 to 3 input nodes and 0 to 3 output nodes. Each input or output node has a specific type, such as DataFrameDirectory, TransformationDirectory, or UntrainedModelDirectory. An input of DataFrameDirectory can only attach to an output of the same type.
* Overfitting: A situation which happens when a trained model latches onto the particular relationships within a training data set, but those particulars are not always indicative of the broader world.
* Pipeline (Azure ML): A collection of components connected together in a defined order. The metaphor represents how data moves from a source (an initial dataset) and flows through components until it reaches a destination. There are two types of pipeline: training pipelines and inference pipelines.
* Pipeline Asset: A component available within Azure Machine Learning. This includes datasets you have imported, sample datasets which come with the service, and different components to transform, train, evaluate, and deploy models.
* Precision: A measure which calculates how frequently our predicted value is correct. It is defined as True Positives / (True Positives + False Positives).
* R^2 (R-squared): An evaluation measure for linear regression models which ranges from 0-1, where 1 is the highest possible score.
* Recall: A measure which calculates how frequently we correctly predict a value. It is defined as True Positives / (True Positives + False Negatives).
* Receiver Operating Characteristic (ROC) curve: A plot which represents true positive versus false positive rates for a two-class model.
* Reinforcement learning: A machine learning technique in which we train an agent to observe its environment and use those environmental clues to make a decision.
* Responsible AI: The Responsible AI project is intended to serve as a framework for promoting ethical behavior when working with and deploying artificial intelligence systems. It consists of six guidelines:
```
    Fairness: AI systems should treat all people fairly and not affect similarly situated groups in different ways.
    Reliability and Safety: Customers should be able to trust that AI solutions will perform reliably and safely within a clear set of parameters, as well as respond safely to unanticipated situations.
    Privacy and Security: AI systems should be secure and respect existing privacy laws.
    Inclusiveness: AI systems should engage and empower people and use inclusive design practices to eliminate unintentional barriers.
    Transparency: People should know how AI systems work and how they interact with data to make decisions.
    Accountability: Those who design and deploy AI systems are accountable for how their systems operate.
```
* Responsible ML: The Responsible ML project is an effort to control machine learning models and protect users. It consists of three key guidelines:
```
    Understand: We should understand our models, including knowing which factors play a role and to what extent they affect the outcome of the model. This ties in quite closely to the Responsible AI guidelines of transparency and fairness.
    Protect: We want to use tools and processes which protect data privacy at all times, even during training.
    Control: We should create audit trails and track the lineage of our models. This will help us ensure that the right model is producing the expected results in a production environment.
```
* Root Mean Square Error (RMSE): An evaluation measure for any regression model. RMSE works best when you are concerned with large differences between the predicted and actual values.
* Root Mean Square Log Error (RMSLE): An evaluation measure for any regression model. RMSLE works best when you are concerned with large percentage differences between the predicted and actual values.
* Run (Azure ML): An attempt to train a model in Azure Machine Learning. This can be done through a pipeline in the Azure ML designer or through Automated ML.
* Semi-supervised learning: A machine learning technique in which we have a small percentage of data with labels and a large percentage of unlabeled data.
* Sink node: A node with no outputs. An example of a sink node is Web Service Output.
* Source node: A node with no inputs. An example of a source node is any dataset you bring onto the canvas.
* Strong Artificial Intelligence: a system which exhibits a human's ability to generalize and solve a variety of problems, including learning how to solve new problems without direct human programming. As of today, there are no strong AI systems in the world, and there remains debate in the academic community around whether strong AI is achievable.
* Super Artificial Intelligence: a system which surpasses a human's ability to generalize and solve problems. This is like strong AI, but the expectation is that the system is superior in every domain of problem-solving capability.
* Supervised learning: A machine learning technique in which we have a known good answer for our label and attempt to learn from this label for inference purposes. The most common examples of this include classification and regression.
* Turing Test: A test where a human tested interacts with two entities, one machine, and one human, without knowing which one is which. The goal of the test is to assess if the tester can identify which one is the machine. If the tester can not determine the machine or is not sure, the machine passes the test.
* Unsupervised learning: A machine learning technique in which we do not have labels for our data. We use unsupervised learning techniques to try to discover what those labels should be. Clustering is the most common example of this.
* Weak Artificial Intelligence: a narrow application of intelligence, focused on solving one problem. An example of this is a system which counts people who enter or leave a bus. All artificial intelligence systems today are considered weak AI.

