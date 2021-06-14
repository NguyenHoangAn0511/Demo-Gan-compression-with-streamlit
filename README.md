# Demo-Gan-compression-with-streamlit
## Member:
Nguyễn Hoàng An - 18520430

Dương Trọng Văn - 18521630
## Installation
Clone this repo
```bash
git clone https://github.com/NguyenHoangAn0511/Demo-Gan-compression-with-streamlit

```
Change directory to Demo-Gan-compression-with-streamlit
```bash
cd your/path/to/Demo-Gan-compression-with-streamlit
```
Create new conda environment
```bash
conda create --name CycleGan
conda activate CycleGan
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
Change directory to Demo-Gan-compression-with-streamlit
```bash
cd your/path/to/Demo-Gan-compression-with-streamlit
```
Use the streamlit web page to view Demo
```bash
streamlit run infer.py
```
