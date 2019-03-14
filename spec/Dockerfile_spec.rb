require 'serverspec'
require 'docker'

describe 'Dockerfile' do
  before(:all) do
    @image = Docker::Image.build_from_dir('.')

    set :os, family: :alpine
    set :backend, :docker
    set :docker_image, @image.id
    # set :docker_container_create_options, {'Entrypoint' => ['ASH']}
  end

  it 'has the working directory set correctly' do
    expect(@image.json["ContainerConfig"]["WorkingDir"]).to eq "/app"
  end

  it 'should have python3 installed' do
    expect(package('python3')).to be_installed
  end

  it 'should have gcc+ installed' do
    expect(package('g++')).to be_installed
  end

  it 'should have app.py installed' do
    expect(file('/app/app.py')).to be_file
  end
end