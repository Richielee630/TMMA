# TMMA: A Tiled Matrix Multiplication Accelerator for Self-Attention Projections in Transformer Models

## Optimized for Edge Deployment on Xilinx KV260

## 🔬 Ongoing Research & Work in Progress
This project is an active research effort, and the implementation is currently under development. We plan to open-source the full code once our research paper is published. Some components may be incomplete or restricted for now.

If you're interested in this project, feel free to watch this repository for updates or reach out for discussions. 🚀

### Overview
TMMA is an FPGA-based accelerator designed to efficiently execute dense matrix multiplication operations, with a primary focus on accelerating the self-attention projection computations in Transformer-based Large Language Models (LLMs). Although our initial goal was to accelerate full DistilBERT inference, development timeline and resource constraints led us to concentrate on optimizing the projection computations (i.e., the matrix multiplications underlying the Q, K, and V projections) in the Multi-Head Self-Attention (MHA) module.

Optimized for resource-constrained edge devices such as the Xilinx KV260 Vision AI Starter Kit, TMMA leverages efficient dataflow, pipelining, and fixed-point arithmetic to achieve a balanced trade-off between resource utilization, latency, and throughput. This makes it a compelling alternative to conventional CPU and GPU-based inference for critical matrix operations.

## Key Features
- **Accelerated Self-Attention Projections**: Optimizes the matrix multiplications critical to the Q, K, and V projections in Transformer models.
- **Edge-Friendly Deployment**: Specifically designed for resource-constrained FPGAs like the Xilinx KV260, enabling on-device inference.
- **Efficient Memory Utilization**: Minimizes external DRAM access by maximizing on-chip BRAM usage through tiling and data reuse strategies.
- **Vivado HLS-Based Implementation**: Developed using high-level synthesis (HLS) for rapid prototyping and iterative design optimizations.
- **Energy Efficiency**: Demonstrates significant energy savings compared to CPU-based implementations, making it suitable for power-constrained applications.

## Project Structure
```plaintext
TMMA/
│── hls/                   # Accelerator source code (Vivado HLS)
│── vivado/                # Vivado design snapshots and constraints
│── models/                # Benchmarking scripts and model integration (e.g., DistilBERT)
│── reference/             # Related reference materials and papers
│── pynq/                  # PYNQ runtime layer and example notebooks (run on KV260)
│── README.md              # This file
│── LICENSE                # License information
```

## Setup and Installation
```bash
git clone https://github.com/yourusername/TMMA.git
cd TMMA
```
1. Follow the instructions in the `hls/` directory to build the accelerator using Vivado HLS.
2. For FPGA deployment, refer to the example notebooks in the `pynq/` directory.

## Benchmarking
Detailed benchmarking scripts and performance evaluations are provided in the `models/` and `pynq/` directories. Our benchmarks include:
- **Standalone GEMM**: Performance evaluation on random matrices.
- **DistilBERT Attention Throughput**: Inference performance when offloading self-attention projection computations to the FPGA.

## Roadmap

### ✅ Completed:
- Systolic Array Design for Matrix Multiplication
- Vivado HLS Implementation
- FPGA Deployment on Xilinx KV260
- Memory Optimization for Edge Deployment

### 🚧 In Progress (Ongoing Research):
- Extending Acceleration to Additional Transformer Components (e.g., Softmax, FFN)
- Expanding Model Compatibility (e.g., GPT-based LLMs)
- Optimizing for Larger Batch Sizes

### 📢 Release
- Code published and tagged as v1.0.0

## References
- **arXiv Paper:** [https://arxiv.org/abs/2503.16731](https://arxiv.org/abs/2503.16731)
- Ashish Vaswani et al., "Attention Is All You Need" (NeurIPS 2017)
- Victor Sanh et al., "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter" (2019)
- S. Lu et al., "Hardware Accelerator for Transformer" (IEEE SOCC 2020) [DOI:10.1109/SOCC49529.2020.9524802](https://ieeexplore.ieee.org/document/9524802)
- Xilinx, "Vitis AI Documentation" (2023)
- Shulin Zeng et al., "FlightLLM: FPGA-Based LLM Acceleration" (FPGA '24)
- Jinming Zhuang et al., "SSR: Spatial Sequential Hybrid Architecture for Latency Throughput Tradeoff in Transformer Acceleration" (FPGA '24)

## Note
This repository does not include compiled bitstreams or full Vivado projects. Users should recreate the hardware platform using the provided HLS code and integration diagrams. Ensure appropriate licenses for any Xilinx IP cores used in your design.

## License
This project is licensed under the MIT License.
