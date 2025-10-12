FROM jekyll/jekyll:latest
USER root
WORKDIR /srv/jekyll
COPY Gemfile* ./
RUN bundle install
COPY . .
RUN gem install sassc
EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--no-watch"]