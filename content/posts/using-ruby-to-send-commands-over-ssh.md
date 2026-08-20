---
title: "Using Ruby to send commands over SSH"
date: 2012-10-23T15:29:00+01:00
draft: false
tags: ["blog-import", "commands", "geek", "linux", "ruby", "ssh"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<br />
Doing a lot of work on remote Linux servers lately, lots of login in over SSH running commands logging out.<br />
<br />
So wrote this simple script to use Ruby to send a single command or a file of commands to a Linux server over SSH. Needs some error trapping etc but functional at the moment.<br />
<br />
It requires the Ruby Gem net-ssh installed.<br />
<br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">#!/usr/bin/ruby</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">require 'rubygems'</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">require 'net/ssh'</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">require 'optparse'</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;"><br /></span>
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">opts = OptionParser.new</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">opts.on("-h HOSTNAME", "--hostname NAME", String, "Hostname of Server") { |v| @hostname = v }</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">opts.on("-u SSH USERNAME", "--username SSH USERNAME", String, "SSH Username of Server") { |v| @username = v }</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">opts.on("-p SSH PASSWORD", "--password SSH PASSWORD", String, "SSH Password of Server") { |v| @password = v }</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">opts.on("-c SHELL_COMMAND", "--command SHELL_COMMAND", String, "Shell Command to Execute") { |v| @cmd = v }</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">opts.on("-f FILE_COMMAND", "--command FILE_COMMAND", String, "File containing shell Commands to Execute") { |v| @fileCmd = v }</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">begin</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; opts.parse!(ARGV)</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">rescue OptionParser::ParseError =&gt; e</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; puts e</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">end</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">raise OptionParser::MissingArgument, "Hostname [-h]" if @hostname.nil?</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">raise OptionParser::MissingArgument, "SSH Username [-u]" if @username.nil?</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">raise OptionParser::MissingArgument, "SSH Password [-p]" if @password.nil?</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">raise OptionParser::MissingArgument, "Command to Execute [-c/-f]" if @cmd.nil? and @fileCmd.nil?</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;"><br /></span>
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">begin</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; ssh = Net::SSH.start(@hostname, @username, :password =&gt; @password)</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; if @cmd != nil then</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; ssh.exec!(@cmd) do |ch, stream, data|</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if stream == :stderr</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; puts "ERROR: #{data}"</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; puts data</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; end</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; end</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; else</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; puts "Processing file #{@fileCmd}"</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; file = File.new(@fileCmd, "r") &nbsp;</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; file.each {|line|&nbsp;</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; ssh.exec!(line) do |ch, stream, data|</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if stream == :stderr</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; puts "ERROR: #{data}"</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; puts data</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; end</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; end</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; &nbsp; &nbsp; }</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; file.close</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; end</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; ssh.close</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">rescue Exception =&gt; e</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; puts "Unable to connect to #{@hostname} using #{@username}/#{@password}"</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">&nbsp; &nbsp; puts e</span><br />
<span style="background-color: white; font-family: Courier New, Courier, monospace; font-size: x-small;">end</span><br />
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a>
</div>
