FROM python:3.12-slim AS app

COPY jail.py /app/run
COPY flag.txt /flag.txt
RUN chmod 555 /app/run && chmod 444 /flag.txt

FROM pwn.red/jail
COPY --from=app / /srv

ENV JAIL_MEM=20M JAIL_PIDS=10 JAIL_PORT=4000 JAIL_TIME=20
