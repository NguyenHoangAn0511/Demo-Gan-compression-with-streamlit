# Demo-Gan-compression-with-streamlit
## Installation

Create new conda environment
```bash
conda create --name CycleGan
```
Use the package manager [conda](https://conda.io/projects/conda/en/latest/index.html) to install Pytorch with GPU.

```bash
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
pip install -r requirements.txt
```
## Run demo
Change directory to the folder where you put infer.py
```bash
cd Demo-Gan-compression-with-streamlit
```
Use the streamlit web page to view Demo
```bash
streamlit run infer.py
```
