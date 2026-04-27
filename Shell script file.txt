#!/bin/bash
echo "Disk usage of the system for root (/) partition:"
df - h| grep '/$'