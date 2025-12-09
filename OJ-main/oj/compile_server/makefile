# 用于对compile模块的自动化的编译
compile_server:compile_server.cc
	g++ -o $@ $^ -std=c++11 -ljsoncpp -lpthread
.PHONY:clean
clean:
	rm -f compile_server