---
title: "Bare bones Arch Linux Install"
date: 2013-07-30T13:25:00+01:00
draft: true
tags: ["blog-import", "geek", "linux"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Something to do at lunchtime to get you more familiar with Linux, create a barebones<a href="https://www.archlinux.org/" target="_blank"> Arch Linux</a> VM. Taken from this article at <a href="http://lifehacker.com/5680453/build-a-killer-customized-arch-linux-installation-and-learn-all-about-linux-in-the-process" target="_blank">Lifehacker </a>I've compressed it into the following steps.<br />
<br />
<ol>
<li>Download image from <a href="https://www.archlinux.org/">https://www.archlinux.org/</a></li>
<li>Partition hard drives /dev/sda1 /dev/sda2 with GParted as ext 4</li>
<li>Boot from ISO and check, setup network <a href="https://wiki.archlinux.org/index.php/Beginners%27_Guide#Wired">https://wiki.archlinux.org/index.php/Beginners%27_Guide#Wired</a></li>
<li>Mount partitions mount /dev/sda1 /mnt ; mkdir /mnt/home; mount /dev/sda2 /mnt/home</li>
<li>mkswap /dev/sda3 ; swapon /dev/sda3</li>
<li>Edit Mirror List vi /etc/pacman.d/mirrorlist</li>
<li>Install base pacstrap -i /mnt base</li>
<li>genfstab -U -p /mnt &gt;&gt; /mnt/etc/fstab</li>
<li>arch-chroot /mnt</li>
<li>nano /etc/locale.gen</li>
<li>echo LANG=en_GB.UTF-8 &gt; /etc/locale.conf</li>
<li>export LANG=en_GB.UTF-8</li>
<li>ln -s /usr/share/zoneinfo/Europe/London /etc/localtime</li>
<li>hwclock --systohc --utc</li>
<li>systemctl enable dhcpcd@eth0.service</li>
<li>passwd</li>
<li>useradd -m -g users -G wheel,storage,power -s /bin/bash alastair</li>
<li>passwd alastair</li>
<li>pacman -S sudo</li>
<li>visudo to uncomment wheel group sudo access</li>
<li>pacman -S grub-bios</li>
<li>grub-install --target=i386-pc --recheck /dev/sda</li>
<li>grub-mkconfig -o /boot/grub/grub.cfg</li>
<li>exit, unmount, reboot</li>
<li>sudo pacman -S alsa-utils</li>
<li>alsamixer ; speaker-test -c 2</li>
<li>pacman -S xf86-video-vesa</li>
<li>pacman -S xorg-server xorg-xinit xorg-server-utils xorg-twm xorg-xclock xterm</li>
<li>sudo pacman -S ttf-dejavu</li>
<li>pacman -S xfce4 xfce4-goodies</li>
<li>systemctl disable fam.service</li>
<li>pacman -Rd fam</li>
<li>pacman -S gamin</li>
<li>cp /etc/skel/.xinitrc ~/.xinitrc ; vi .xinitrc</li>
<li>pacman -S openssh</li>
<li>startx </li>
</ol>
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
