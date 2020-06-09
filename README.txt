The data for our model is under data. For more information on the variables please see the technical report pdf file.

The model is created using JMP. Before the final model was created new variables were formed. The methodology section in the pdf will explain
how we got the variables. The data along with the new variables used can be found in JMP_data.

Although JMP was used, other software can be used to achieve the same result. The model was formed by using a standard least regression using 
Risk_Score_Tentative as the 'y' and other variables (labelled in the pdf) as the inputs.
If using JMP it can be done by Analyze-> Fit Model -> Risk_Score_Tentative to y -> Other Variables to Add -> Run
The model is formed and the prediction formula was saved to the data table which was used to calculate a risk score for all neighborhoods.
Standard Least Squares -> Save Columns -> Prediction Formula

The model and data script is located in Risk_Score_Model JMP file.

The results of the model is found in Risk_Score+Category csv file.