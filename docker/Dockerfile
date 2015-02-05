FROM froskekongen/tgather_base
MAINTAINER froskekongen <erlend.aune.1983@gmail.com>

ENV LANG C.UTF-8

RUN git clone https://github.com/Froskekongen/tgather
RUN chmod +x /tgather/tgather.py


ENTRYPOINT ["/tgather/tgather.py"]
