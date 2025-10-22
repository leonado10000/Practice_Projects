import wandb
import weave
from linear_regression_scratch import model, mse, sgd, X, y

WANDB_API_KEY = "f23a0839fa5de5085785818ab4c16be0f7be4ed9"

wandb.init(
    project="quickstart-playground",
    config={
        "lr": 0.01,
        "epochs": 100,
        "input_dim": 4,
        "output_dim": 4, 
    }
)

for epoch in range(100):
    y_pred = model(X)
    loss = mse(y_pred, y)
    loss.backward(X)
    sgd.step()

    # 🟢 Log values to W&B
    wandb.log({"epoch": epoch, "loss": loss.loss})

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")
