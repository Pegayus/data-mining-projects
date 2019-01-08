%generate a random dataset and calculate min and MAX of the distance
for n=508:1000
    for d=1:100
        data=rand(n,d);
        M=0;
        m=inf;
        for i=1:n
           for j=i+1:n
              dist=norm(data(i,:)-data(j,:));
              %dist=norm(data(i,:)-data(j,:),1);
              if dist>M
                  M=dist;
              end
              if dist<m
                  m=dist;
              end
         
           end
        end
        gamma=log((M-m)/m); %log distance
        x=[x;n];
        y=[y;d];
        z=[z;gamma];
    
    end
    
end

%plot
matrix = [x y z];
tri = delaunay(matrix(:,1),matrix(:,2));
trisurf(tri,matrix(:,1),matrix(:,2),matrix(:,3))
shading interp
title('curse of dimensionality');
ylabel('features');
xlabel('instances');
zlabel('gamma');
set(get(gca,'xlabel'),'rotation',15);
set(get(gca,'ylabel'),'rotation',-28);

