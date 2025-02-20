# SAMA: Systolic Array Matrix Accelerator for LLMs

## Overview
SAMA (**S**ystolic **A**rray **M**atrix **A**ccelerator) is an FPGA-based accelerator designed for matrix multiplication in Transformer-based **Large Language Models (LLMs)**. This project optimizes **dense matrix operations** crucial for attention mechanisms and feedforward layers, targeting resource-constrained **edge devices** such as the **Xilinx KV260 Vision AI Starter Kit**.

By leveraging **efficient dataflow, pipelining, and fixed-point arithmetic**, SAMA provides a **balanced trade-off between resource utilization, latency, and throughput**, making it a compelling alternative to CPU and GPU-based inference.

## Key Features
- **Optimized for Transformer Workloads**: Directly accelerates matrix multiplications (e.g., Q, K, V, Output Projections) within attention mechanisms.
- **Edge-Friendly Deployment**: Designed for resource-constrained FPGAs like Xilinx KV260, unlike prior work targeting high-end FPGA platforms.
- **Efficient Memory Utilization**: Minimizes external DRAM access by **maximizing on-chip BRAM usage** through **tiling and data reuse**.
- **Vivado HLS-Based Implementation**: Developed using **high-level synthesis (HLS)** for ease of development and optimization.

## Project Structure
```
SAMA/
│── hls/                   # Accelerator source code (Vivado HLS)
│── models/                # Transformer model benchmarks
│── reference/             # Reference Paper
│── experiments/           # Performance comparison scripts
│── docs/                  # Documentation and reports
│── hardware/              # FPGA configurations and deployment scripts
│── results/               # Benchmarking results and comparisons
│── README.md              # This file
│── LICENSE                # License information
```

## Setup and Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/SAMA.git
   cd SAMA
   ```

## Benchmarking


## Roadmap
- [x] Systolic Array Design for Matrix Multiplication
- [x] Vivado HLS Implementation
- [x] FPGA Deployment on Xilinx KV260
- [ ] Memory Optimization for Edge Deployment
- [ ] Further Model Compatibility (e.g., GPT-based LLMs)

## Contributors
- **Richie Li** ([zhaoqil3@uci.edu](mailto:zhaoqil3@uci.edu)) – FPGA Design & Implementation
- **Sicheng Chen** ([sichenc5@uci.edu](mailto:sichenc5@uci.edu)) – Model Benchmarking & Validation

## References
- Ashish Vaswani et al., *Attention Is All You Need* (NeurIPS 2017)
- Xilinx, *Vitis AI Documentation* (2023)
- Shulin Zeng et al., *FlightLLM: FPGA-Based LLM Acceleration* (FPGA '24)

## License
This project is licensed under the **MIT License**.
