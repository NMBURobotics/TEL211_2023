#!/bin/bash
Recipient="fetulahatas1@gmail.com"
Subject="Greeting"
Message="This is spam"
`mail -s $Subject $Recipient <<< $Message`
