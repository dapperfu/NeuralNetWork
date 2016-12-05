while [ 1 ];
do
git add *.ipynb
git commit -a -m "Git Auto Commit: `date`"
#git push
sleep 300
done
